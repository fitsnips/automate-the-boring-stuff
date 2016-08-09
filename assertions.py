#! python3

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry Dave. I\'m affraid I can not do that.'
assert podBayDoorStatus == 'open',  'The pod bay doors need to be "open".'