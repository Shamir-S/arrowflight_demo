FROM mambaorg/micromamba:0.23.3

ARG MAMBA_DOCKERFILE_ACTIVATE=1
USER $MAMBA_USER


# RUN micromamba install pyarrow=11.0.0 libgrpc=1.57 -c conda-forge
RUN micromamba install pyarrow=13.0.0 libgrpc=1.58 -c conda-forge


WORKDIR /app
COPY client.py .

CMD ["python", "client.py"]
