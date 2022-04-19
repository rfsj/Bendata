"""
export_as_pdf = st.button(“Export Report”)

if export_as_pdf:
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url("http://XX.XXX.XXX.XXX:XXXX", "dashboard.pdf", configuration=config) #Blank page
    pdfkit.from_url("google.fr", "google.pdf", configuration=config) #It works
    """