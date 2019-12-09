

# from io import BytesIO, StringIO
# from django.http import HttpResponse, response
from django.template.loader import get_template
from django.template import Context

# # import StringIO
# from xhtml2pdf import pisa
# # from pandas.compat import StringIO

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     # result = BytesIO()
#     result = StringIO()
#     pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result)
#     # pdf = pisa.CreatePDF(html.encode('UTF-8'), response, encoding='UTF-8')

#     pdf = pisa.pisaDocument(StringIO(html), result, encoding='UTF-8')
#     # pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result, encoding='UTF-8')
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
from Housing import settings

def get_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context_dict)

    import subprocess
    wkhtml2pdf = subprocess.Popen((settings.WKHTML2PDF_COMMAND,
                                   "--footer-right",
                                   "[page]/[toPage]",
                                   "--print-media-type",
                                   "--encoding",
                                   "UTF-8",
                                   "-",
                                   "-"),
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE)
    wkdata = wkhtml2pdf.communicate(html.encode('utf8'))
    pdf = wkdata[0];

    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=printfile.pdf'
    response.write(pdf)
    return response