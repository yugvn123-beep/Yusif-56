from kivy.lang import Builder
from kivymd.app import MDApp

# الكود الأول مضافاً إليه الشريط العلوي للأيقونة
v7x = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        
        # هنا أضفنا الشريط العلوي والأيقونة والعنوان
        MDTopAppBar:
            title: "تطبيقي الأول"
            anchor_title: "center"
            left_action_items: [["android", lambda x: None]]
            elevation: 2
            
        MDFloatLayout:
            # الكود الأول الخاص بك كما هو بدون تغيير
            MDFloatingActionButtonSpeedDial:
                data: app.row
                rotation_root_button: True
'''

class Myapp(MDApp):
    row = {
        'Python': 'language-python',
        'Android': 'android',
    }

    def build(self):
        # لتغيير أيقونة التطبيق الرسمية عند التثبيت (اختياري)
        self.icon = 'icon.png' 
        return Builder.load_string(v7x)

Myapp().run()
