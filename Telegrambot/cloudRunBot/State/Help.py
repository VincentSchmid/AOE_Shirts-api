from .State import State


class Help(State):
    def stateInit(self):
        self.model.clear_data()

        self.send_message("When you send /start the process will be begin")
        self.send_message("you can allways send /start to reset the process to the beginning")
        self.send_message("First you send the background of your post (AOE screenshot size: 1080x1080)")
        self.send_message("Next you will send the unedited photos of your shirt. Send as many pictures of your shirt as you want")
        self.send_message("Once you're done sending your shirt images, confirm by sending the command /done")
        self.send_message("From now on, the bot will take over and process your images. It will crop out the shirts and place them on your background image and send the result as files")
        self.send_message("send /start to begin")
        