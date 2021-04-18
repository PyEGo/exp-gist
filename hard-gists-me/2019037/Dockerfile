FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","trytonar_account_invoice_ar"]
RUN ["pip","install","fio_shipping_gls"]
RUN ["pip","install","openlabs_shipping"]
RUN ["pip","install","openlabs_payment_gateway"]
RUN ["pip","install","trytond-account-dunning"]
CMD ["python","snippet.py"]

