abc = "abcdefghijklmnopqrstuvwxyz"

def get_user_input():
    user_input = input()
    try:
        val = int(user_input)
        return val
    except ValueError:
        try:
            val =  float(user_input)
            return val
        except ValueError:
            try:
                val =  bool(user_input)
                return val
            except ValueError:
                val = str(user_input)
                return val


