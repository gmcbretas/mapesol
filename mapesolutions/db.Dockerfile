FROM mdillon/postgis:10
RUN apt-get update && \
    apt-get install -y \
      cmake \
      git
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      libxml2-dev \
      zlib1g-dev \
      unzip \
      g++ \
      libpq-dev \
      postgresql-server-dev-10 \
      zip \
      libcunit1 \
      libcunit1-dev \
      libcunit1-doc \
      postgresql-plpython-10 \
      libgdal20 \
      libgdal-doc \
      libgdal-dev \
      gdal-bin \
      libboost-graph-dev \
      libcgal-dev
RUN cd /tmp && git clone https://github.com/pgRouting/pgrouting.git && \
    cd pgrouting && \
    git checkout v2.6.0 && \
    mkdir build && \
    cd build && \
    cmake \
#        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE="Release" \
        .. && \
    make && \
    make install && \
    rm -rf /tmp/pgrouting
RUN cd /tmp && git clone  https://github.com/hobu/laz-perf.git \
    && cd laz-perf \
    && git checkout 62632b19ebbe1b72a82f6c652a3687b9466c006e \
    && mkdir build \
    && cd build \
    && cmake \
#        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE="Release" \
        .. \
    && make \
    && make install \
    && rm -rf /tmp/laz-perf
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      autoconf \
      automake
RUN cd /tmp && git clone https://github.com/pgpointcloud/pointcloud.git\
    && cd /tmp/pointcloud \
    && git checkout 29fdb7cb504e57f7ccbf18e9c16cab8ec53ad884 \
    && ./autogen.sh && ./configure --with-pgconfig=/usr/bin/pg_config \
    && make \
    && make install \
    && rm -rf /tmp/pointcloud
RUN cd /tmp && git clone https://github.com/pramsey/pgsql-ogr-fdw.git \
    && cd /tmp/pgsql-ogr-fdw \
    && git checkout 2d6aa7a42b94cc6b3f541fb8835ee85c7091450b \
    && make \
    && make install \
    && rm -rf /tmp/pgsql-ogr-fdw

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb-pgrouting.sh /docker-entrypoint-initdb.d/routing.sh