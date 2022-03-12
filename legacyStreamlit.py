#try: 
    #os.makedirs(filename)
#except OSError:
    #if os.path.isdir(filename):
        #st.write('Cannot access this entry')
        #st.write("Try to change file in -- 'Select a file'")
        #st.stop()
    #elif not pd.errors.ParserError:
     #   st.write('Caaa')
#except Exception as e:    
 #       errortype = e.message.split('.')[0].strip()                                
  #      if errortype == 'Error tokenizing data. C error': 
  #          st.stop()