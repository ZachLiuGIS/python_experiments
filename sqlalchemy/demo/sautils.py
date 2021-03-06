from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import ClauseElement


def get_or_create(session, model, defaults=None, **kwargs):
    try:
        instance = session.query(model).filter_by(**kwargs).one()
        return instance, False

    except NoResultFound:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        return instance, True
