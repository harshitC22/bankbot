"""
written by: harshit C
"""

"""
manages state of chat bot
"""
class The_BOT:

    """
    class variables
    """
    state_list= ["sleep", "awake", "greeted", "requirement_Asked"]
    states= enumerate (state_list)

    """
    initialize state variable
    """
    def __init__ (self):

        """
        all the following functions change the state of the bot
        """



    def wake_up (self):

        self.state= "awake"
        return self.state

    def user_greeted (self):

        self.state= "greeted"
        return self.state

    def get_state (self):

        return self.state

    def set_state (self, state):

        self.state= state
