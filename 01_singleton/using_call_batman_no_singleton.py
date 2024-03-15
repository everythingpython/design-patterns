from call_batman_no_singleton import batman_obj, Batman

batman_obj.who_am_i()

batman_obj2 = Batman()
print(batman_obj is batman_obj2)  # Returns False
