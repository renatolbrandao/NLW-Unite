from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError

db_connection_handler.connect_to_db()

class CheckInRepository:
    def insert_check_in(self, attendee_id):
        try:
            with db_connection_handler as database:
                check_in = {
                    CheckIns(attendeeId = attendee_id)
                }
                database.session.add(check_in)
                database.session.commit()
        except IntegrityError:
            raise Exception('Check In ja cadastrado!')
        except Exception as exception:
            database.session.rollback()
            raise exception
