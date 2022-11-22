from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

class UserController:
    @staticmethod()
    def user_controller_get():
        try {

        } except DuplicateKeyError {
            HTTPException(
              status_code=404, 
              detail="Constraint key database."
            )
        }