from tkinter import * 

class MainImage:
    def __init__(self, location):
        self.mainCanvas = Canvas(location, width=200, height=200)
        self.mainCanvas.pack()
        self.imageList = []
        self.imageList.append(PhotoImage(file='src/phase_0.png'))
        self.imageList.append(PhotoImage(file='src/phase_1.png'))
        self.imageList.append(PhotoImage(file='src/phase_2.png'))
        self.imageList.append(PhotoImage(file='src/phase_3.png'))
        self.imageList.append(PhotoImage(file='src/phase_4.png'))
        self.imageList.append(PhotoImage(file='src/phase_5.png'))
        self.imageList.append(PhotoImage(file='src/phase_6.png'))
        self.imageList.append(PhotoImage(file='src/phase_7.png'))
        self.currImageID = 0
        self.imageCanvas = self.mainCanvas.create_image(0,0, anchor=NW, image=self.imageList[self.currImageID])
       

    def displayCanvasImage(self, imageId):
        if (imageId < 0) or (imageId > 7):
            return
        else:          
            self.currImageID = imageId
            self.mainCanvas.itemconfig(self.imageCanvas, image=self.imageList[self.currImageID])
    

        