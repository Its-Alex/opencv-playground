# Opencv python playground

This repository is used to perform some tests on opencv library.

## Requirements

- [mise](https://mise.jdx.dev/)

After installing dependencies, execute:

```sh
$ mise trust && mise install
```

## Getting started

Some scripts are available in [src](./src) to tests some features.

### VideoReader RTSP

You can open a RTSP stream using:

```sh
$ python src/open-rtsp-stream.py <rtsp-url>
```
To enable OpenCV debug you can use:

```sh
export OPENCV_LOG_LEVEL=DEBUG
export OPENCV_VIDEOIO_DEBUG=1
export OPENCV_VIDEOCAPTURE_DEBUG=1
export OPENCV_VIDEOWRITER_DEBUG=1
export OPENCV_FFMPEG_DEBUG=1
export OPENCV_FFMPEG_LOGLEVEL=56 # https://ffmpeg.org/ffmpeg.html#:~:text=including%20debugging%20information.-,%E2%80%98trace%2C%2056%E2%80%99,-For%20example%20to
```

## Licence

[MIT](./LICENSE)