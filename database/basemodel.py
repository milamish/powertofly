import datetime
import decimal
import logging

from config import Config
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URI = Config.SQLALCHEMY_DATABASE_URI
engine = create_engine(DB_URI, echo=False)
SqlAlchemySession = sessionmaker(bind=engine)


logger = logging.getLogger(__name__)


class BaseModel(declarative_base()):
    user_id = Column(Integer, primary_key=True)
    __abstract__ = True

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if type(value) not in [str, dict, datetime.datetime, datetime.date, float, decimal.Decimal, list, tuple]:
                value = str(value)
            d[column.name] = value
        return d


class BaseRepository:
    model = None

    def __init__(self, session):
        self.session = session

    def get_count(self):
        return self.session.query(self.model).count()

    def get_record_with_id(self, model_id):
        return self.session.query(self.model).filter(self.model.id == model_id).first()

    def get_records_with_ids(self, ids_):
        return self.session.query(self.model).filter(self.model.id.in_(ids_)).all()

    def get_all_records(self, limit=100):
        query = self.session.query(self.model).order_by(self.model.user_id.desc())
        return query.all() if limit == 0 else query.limit(limit).all()

    def create_record(self, values):
        obj = self.model(**values)
        self.session.add(obj)
        self.session.flush()
        return obj

    def update_record_with_id(self, record_id, **kwargs):
        self.session.query(self.model).filter(self.model.id == record_id).update(kwargs)
        self.session.flush()

    def bulk_update_records_with_ids(self, record_ids, **kwargs):
        self.session.query(self.model).filter(self.model.id.in_(record_ids)).update(kwargs)
        self.session.flush()

    def bulk_create_record(self, values: list):
        try:
            self.session.bulk_insert_mappings(self.model, values)
        except Exception as ex:
            logger.error(ex)
        self.session.flush()

    def get_record_with_(self, **kwargs):
        return self.session.query(self.model).filter_by(**kwargs).first()

    def get_latest_record_with_(self, **kwargs):
        return self.session.query(self.model) \
            .filter_by(**kwargs) \
            .order_by(self.model.write_date.desc()).first()

    def get_record_count_with_(self, **kwargs):
        return self.session.query(self.model).filter_by(**kwargs).count()

    def get_all_record_with_(self, limit=None, **kwargs):
        queryset = self.session.query(self.model).filter_by(**kwargs)
        if limit:
            queryset = queryset.limit(limit)
        return queryset.all()
