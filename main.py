from src.bayesdice import BayesDice

bd = BayesDice()
bd.choose_die()

for i in range(10):
    roll = bd.roll_die()
    bd.update_priors(roll)
