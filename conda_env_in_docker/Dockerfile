FROM mambaorg/micromamba:2.0.2

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yaml /tmp/environment.yaml

# install environment as base env
# base gets activated automatically
RUN micromamba install -y -n base -f /tmp/environment.yaml && \
    micromamba clean --all --yes

