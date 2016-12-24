import time
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.pagelayout import PageLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import ObjectProperty
from kivy.core.image import Image
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.lang import Builder
from kivy.app import App 
from kivy.uix.screenmanager import Screen, ScreenManager , FadeTransition
#from kivy.uix.camera import Camera
from plyer.facades import camera
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

Builder.load_string(
'''
<StartScreen>:
	GridLayout:
		cols: 2
		Button:
			# text: "Button 1"
			on_press: root.manager.current = "camera"
			background_color: (0,1,0,0.5)
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'icon.png'
					pos: self.pos
					size: self.size
		Button: 
			# text: "Button 2"
			on_press: root.manager.current = "audio"
			background_color: (0,1,0,0.5)
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'music_icon.png'
					pos: self.pos
					size: self.size
		Button:
			# text: "Button 3"
			background_color: (0,1,0,0.5)
			on_press: root.manager.current = "gallery"
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'gallery.png'
					pos: self.pos
					size: self.size
		Button:
			text: "Button 4"
			background_color: (0,1,0,0.5)

<CameraScreen>:
	BoxLayout:
		orientation: "vertical"
		Camera:
			id: camera
			resolution: (1024, 1024)

		Button:
			size_hint: None,None
			width: '80dp'
			height: '80dp'
			pos: self.pos
			background_color: 0, 1, 0, 0.5
			on_press: root.manager.current = "start"
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image:
					source: 'back.png'
					pos: self.pos
					size: self.size
	
		Button:
			# text: "Capture photo"
			size_hint: None, None
			width: '80dp'
			height: '80dp'
			background_color: 255, 255, 255, 0.3
			on_press: root.click_pic()
			# pos_hint: 0.25	
			# pos: self.parent.x*0.25, self.parent.y
			BoxLayout:
				pos: self.parent.pos
				size: self.parent.size
				Image: 
					source: 'capture.png'
					pos: self.pos
					size: self.size
		
<GalleryScreen>:
	name: "gallery"
	BoxLayout:
		id: gallery_layout
		Button: 
			on_press: root.AddImage()	

<AudioScreen>:
	GridLayout:
		cols: 2
		Button:
			text: "hello"
			on_press: root.playmusic()
''')
camera = ObjectProperty(None)
gallery_layout = ObjectProperty(None)
class StartScreen(Screen):
	pass
class AudioScreen(Screen):
	def playmusic(self):
		fname = 'example.wav'
		sound = SoundLoader.load(fname)
		# if sound is not None:
			# print "played"
			# sound.play()
		# else:
		# 	print "Doesn't exist"
class CameraScreen(Screen):
	
	# def changei(x):
	# 	return str(int(x) + 1)
	
	def click_pic(self):
		camera = self.ids['camera']
		timestr = time.strftime("%d-%m-%Y_%H:%M:%S")
		camera.export_to_png("IMG_" + timestr)
		print "Captured"
		print time.strftime("%d%m%Y_%H%M%S")
class GalleryScreen(Screen):
	# def __init__(self):
	# 	self.AddImage()
	def AddImage(self):
		gallery_layout = self.ids['gallery_layout']
		# for i in range(0,11):
		# 	im = Image(source='gallery.png')
		# 	gallery_layout.add_widget(im)


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name="start"))
sm.add_widget(CameraScreen(name="camera"))
sm.add_widget(GalleryScreen(name="gallery"))
sm.add_widget(AudioScreen(name="audio"))
class CameraApp(App):
	sm.current = "start"
	def build(self):
		return sm
CameraApp().run()