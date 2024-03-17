ARG PORT 8000
FROM cypress/browser:latest
RUN apt-get install python 3 -y
RUN echo $(python3 -m site --user)
COPY requirements.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN at-get update && apt-get install -y python3-pip && pip install -r requirements.txt
COPY . .
CMD [ "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "$PORT" ]