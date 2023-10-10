"""
This is a couple of examples for SQLAlchemy 2.0
"""
from typing import List, Optional

import sqlalchemy
from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

"""
Declaring Tables is roughly done like so
"""


class Base(DeclarativeBase):
    """
    This is the base class for tables.
    It can contain some stuff for all tables that inherit this.
    But for most cases, I guess it might be left blank
    """

    pass


class Customer(Base):
    """
    Sample table that will contain some details about fictional customers
    """

    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    full_name: Mapped[Optional[str]]

    email: Mapped[List["Email"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        """
        This will be how this class would be 'printed' out if it is printed
        or represented as a string
        """
        return f"User(id={self.id!r}, name={self.name!r})"


class Email(Base):
    """
    Sample table that contains emails of the above fictional customers
    """

    __tablename__ = "email"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))

    user: Mapped["Customer"] = relationship(back_populates="email")

    def __repr__(self):
        return f"Email(id={self.id!r}, email_address={self.email_address!r})"


engine = create_engine("sqlite:///sqlalchemy2example.db", echo=True)
Base.metadata.create_all(engine)


def simple_insert():
    with Session(engine) as session:
        spongebob = Customer(
            name="spongebob",
            full_name="Spongebob Squarepants",
            email=[
                Email(email_address="spongebob@random.io"),
            ],
        )
        sandy = Customer(
            name="sandy",
            full_name="Sandy Cheeks",
            email=[
                Email(email_address="sandy@random.io"),
                Email(email_address="sandy@anotherdomain.com"),
            ],
        )
        patrick = Customer(
            name="Patrick",
            full_name="Patrick Star",
        )

        session.add_all([spongebob, sandy, patrick])
        session.commit()


def simple_query():
    with Session(engine) as session:
        result = session.scalars(
            select(Customer).where(Customer.name.in_(["spongebob", "sandy"]))
        )
        for user in result:
            print(user)
