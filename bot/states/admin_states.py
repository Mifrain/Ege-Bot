from aiogram.dispatcher.filters.state import State, StatesGroup

class AddAdminState(StatesGroup):
    adm_id = State()
    
    
class AddProtState(StatesGroup):
    new_prot = State()
    
class DelProtState(StatesGroup):
    del_prot = State()
    

class AddMatState(StatesGroup):
    new_mat = State()
    
class DelMatState(StatesGroup):
    del_mat = State()
    

class SendSpamState(StatesGroup):
    send = State()