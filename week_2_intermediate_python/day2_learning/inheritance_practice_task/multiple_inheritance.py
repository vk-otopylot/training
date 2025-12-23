# Teacher and Researcher to Professor Role

# class Teacher:
#     def __init__(self, subject):
#         self.subject = subject
#
# class Researcher:
#     def __init__(self, r_area, subject):
#         super().__init__(subject)
#         self.r_area = r_area
#
# class Professor(Researcher, Teacher):
#     def __init__(self, name, r_area, subject):
#         super().__init__(r_area, subject)
#         self.name = name
#
#     def display_profile(self):
#         print(f'Name: {self.name}, Subject: {self.subject}, Research_area: {self.r_area}')
#
# prof1 = Professor('vivek k', 'History', 'History')
# prof1.display_profile()

# Camera and Music Player to Smartphone

# class Camera:
#     def take_photo(self):
#         print('Photo taken')
#
# class MusicPlayer:
#     def play_music(self):
#         print('Music Started')
#
# class SmartPhone(Camera, MusicPlayer):
#     def use_features(self):
#         self.take_photo()
#         self.play_music()
#
# sp1 = SmartPhone()
# sp1.use_features()