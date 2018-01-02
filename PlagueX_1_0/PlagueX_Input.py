class fileinput:
    """The purpose of this class is to extract ".pdf", ".docx" and"""
    """".doc" files from the given directory and return the refined text without headers"""
    """footers, page numbers, titles, headings and any unwanted strings"""

    
    from io import StringIO
    import docx2txt
    sentlist = []
    def __init__(self,filename):
        """ The init method of class fileinput takes the filename as an argument"""
        """ and initialises the attribute self.name"""
        self.name = filename
        
    def docxtract(self):
        """Extracts the text from ".docx" and ".doc" files returns the unrefined text"""
        self.text = self.docx2txt.process(self.name)
        return(self.text)
    
    def pdfxtract(self):
        """Extracts the text from ".pdf" files and returns the unrefined text"""
        from pdfminer.pdfparser import PDFParser, PDFDocument
        from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
        from pdfminer.converter import PDFPageAggregator
        from pdfminer.layout import LAParams, LTTextBox, LTTextLine
        fp = open(self.name, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        text = ""
        # Process each page contained in the document.
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    text+=str(lt_obj.get_text())
        return(text)
        
    def fileconvert(self):
        """Checks whether the file is ".docx" or ".pdf" and passes the filename"""
        """into the respective function depending on the file format to get the"""
        """unrefined text"""
        if self.name[-5:]==".docx" or self.name[-4:]==".doc":
            try:
                self.docxtract()
            except:
                return(0)
            return(self.docxtract())

        elif self.name[-4:]==".pdf":
            try:
                self.pdfxtract()
            except:
                return(0)
            return(self.pdfxtract())
        
    def textrefine(self):
        """Refines the text and removes the unwanted strings from the text like the header,"""
        """footer, page number, headings and title""" 
        
        self.raw = self.fileconvert()
        self.sentx = []
        for char in range(len(self.raw)):
            try:
                if (self.raw[char]== "\n" or self.raw[char]== "\t") and (self.raw[char+1]!= "\n" or self.raw[char+1]!= "\t"):
                    numb = 1
                    while (self.raw[char+numb]) != "\n" and (self.raw[char+numb]) != "\t":
                        numb+=1
                    if (self.raw[char+numb-1] != " " and self.raw[char+numb-1] != " "):
                        self.sentx.append(self.raw[char+1:char+numb]+" ")
                    else:
                        self.sentx.append(self.raw[char+1:char+numb])
            except IndexError:
                    self.sentx.append(self.raw[char+1:])
                    break
        
        self.sentx = [x for x in self.sentx if not (len(x)<3 or (len(x)<20 and not x[0].islower()))]
        return("".join(self.sentx))


    

