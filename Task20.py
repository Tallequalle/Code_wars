#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
def make_readable(seconds):
    # Do something
    if 10 <= seconds < 60:
        return "00:00:{}".format(seconds)
    elif 10 > seconds:
        return "00:00:0{}".format(seconds)
    elif 60 <= seconds < 600:
        if seconds // 60 < 10:
            if seconds % 60 < 10:
                return f'00:0{seconds // 60}:0{seconds % 60}'
            elif seconds % 60 >= 10:
                return f'00:0{seconds // 60}:{seconds % 60}'
        elif seconds // 60 >= 10:
            if seconds % 60 < 10:
                return f'00:{seconds // 60}:0{seconds % 60}'
            elif seconds % 60 >= 10:
                return f'00:{seconds // 60}:{seconds % 60}'
    elif 600 <= seconds < 3600:
        if seconds % 60 < 10:
            return f'00:{seconds // 60}:0{seconds % 60}'
        elif seconds % 60 >= 10:
            return f'00:{seconds // 60}:{seconds % 60}'
    elif 3600 <= seconds <= 360000:
        if seconds // 3600 < 10:
            if (seconds % 3600) // 60 < 10:
                if ((seconds % 3600) % 60) < 10:
                    return f'0{seconds // 3600}:0{(seconds % 3600) // 60}:0{((seconds % 3600) % 60)}'
                elif ((seconds % 3600) % 60) >= 10:
                    return f'0{seconds // 3600}:0{(seconds % 3600) // 60}:{((seconds % 3600) % 60)}'
            elif (seconds % 3600) // 60 >= 10:
                if ((seconds % 3600) % 60) < 10:
                    return f'0{seconds // 3600}:{(seconds % 3600) // 60}:0{((seconds % 3600) % 60)}'
                elif ((seconds % 3600) % 60) >= 10:
                    return f'0{seconds // 3600}:{(seconds % 3600) // 60}:{((seconds % 3600) % 60)}'
        elif seconds // 3600 >= 10:
            if (seconds % 3600) // 60 < 10:
                if ((seconds % 3600) % 60) < 10:
                    return f'{seconds // 3600}:0{(seconds % 3600) // 60}:0{((seconds % 3600) % 60)}'
                elif ((seconds % 3600) % 60) >= 10:
                    return f'{seconds // 3600}:0{(seconds % 3600) // 60}:{((seconds % 3600) % 60)}'
            elif (seconds % 3600) // 60 >= 10:
                if ((seconds % 3600) % 60) < 10:
                    return f'{seconds // 3600}:{(seconds % 3600) // 60}:0{((seconds % 3600) % 60)}'
                elif ((seconds % 3600) % 60) >= 10:
                    return f'{seconds // 3600}:{(seconds % 3600) // 60}:{((seconds % 3600) % 60)}'
make_readable(86399)
