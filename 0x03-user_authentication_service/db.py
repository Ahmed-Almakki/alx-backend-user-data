#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """save the user to the database
        """
        session = self._session
        s = User()
        s.email = email
        s.hashed_password = hashed_password
        session.add(s)
        session.commit()
        return s

    def find_user_by(self, *args, **kwargs) -> User:
        """
        find the first row of the requested query
        :param args: parametrs as a list
        :param kwargs: parameters as a dictionary
        :return: first record
        """
        for key, value in kwargs.items():
            pass
        users = self._session.query(User).where(User.email == value).\
            first()
        if users is None:
            raise NoResultFound("Not Found")
        if key not in [c.key for c in User.__table__.c]:
            raise InvalidRequestError("Invalid request")
        return users
