from model_utils import Choices
TYPE_TABLE = Choices(
    ('family', 'Family'),
    ('individual', 'Individual'),
    ('couples', 'Couples'),
    ('friends', 'Friends')

)
STATUS_TABLES = Choices(
    ('available', 'Available'),
    ('occupied', 'Occupied'),
    ('reserved', 'Reserved'),
    ('waiting', 'Waiting'),
    ('cleaning', 'Cleaning'),
    ('out_of_service', 'Out of service'),
)

QUANTITY = Choices(
    (1 ,'one'),
    (2 ,'two'),
    (4 , 'four'),
    (6 ,'six'),
)

STATUS_R = Choices(

    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
    ('no_show', 'No Show'),
    ('waiting', 'Waiting'),

)