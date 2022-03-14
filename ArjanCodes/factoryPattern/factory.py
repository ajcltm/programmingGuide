from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, Type

class VideoExporter(Protocol):
    """Basic representation of video exporting codec."""
    
    def prepare_export(self, video_data:str) -> None:
        """Prepares video data for exporting"""

    def do_export(self, folder: Path) -> None:
        """Exports video data to a folder."""

class LosslessVideoExporter:
    """Lossless video exporting codec."""

    def prepare_export(self, video_data:str) -> None:
        print("Preparing video data for lossless export")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in lossless format to {folder}")


class H264BPVideoExporter:
    """H.264 video exporting codex with BaseLine profile"""

    def prepare_export(self, video_data:str) -> None:
        print("Preparing video data for H.264 (BaseLine) export")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (BaseLine) format to {folder}")

class H264Hi422PVideoExporter:
    """H.264 video exporting codex with Hi422P profile (10-bit, 4:2:2 chroma sampling)"""

    def prepare_export(self, video_data:str) -> None:
        print("Preparing video data for H.264 (Hi422P) export")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}")


class AudioExporter(Protocol):
    """Basic representation of audio exporting codec"""

    def prepare_export(self, audio_data: str) -> None:
        """Prepares audio data for exporting"""

    def do_export(self, folder: Path) -> None:
        """Exports the audio data to a folder"""


class AACAudioExporter:
    """AAC audio exporting codec"""

    def prepare_export(self, audio_data: str) -> None:
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in AAC format to {folder}")

class WAVAudioExporter:
    """WAV (lossless) audio exporting codec"""
    
    def prepare_export(self, audio_data: str) -> None:
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in WAV format to {folder}")


@dataclass
class MediaExporter:
    video : VideoExporter
    audio : AudioExporter

@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audio_class: Type[AudioExporter]

    def __call__(self) -> MediaExporter:
        return MediaExporter(self.video_class(), self.audio_class())

FACTORIES = {
    "low": MediaExporterFactory(H264BPVideoExporter, AACAudioExporter),
    "high": MediaExporterFactory(H264Hi422PVideoExporter, AACAudioExporter),
    "master": MediaExporterFactory(LosslessVideoExporter, WAVAudioExporter)
}

def read_factory() -> MediaExporterFactory:
    """Constructs an exporter factory based on the user's preference."""

    while True:
        export_quality = input(
            f"Enter desired output quality ({', '.join(FACTORIES)}): " 
        )
        try:
            return FACTORIES[export_quality]
        except KeyError:
            print(f"Unknown output quality option: {export_quality}")

def do_export(exporter: MediaExporter) -> None:
    """Do a test export using a video and audio exporter"""

    # prepare the export
    exporter.video.prepare_export('placeholder_for_video_data')
    exporter.audio.prepare_export('plaveholder_for_audio_data')

    # do the export
    folder = Path("/usr/tmp/video")
    exporter.video.do_export(folder)
    exporter.audio.do_export(folder)

def main():
    # create the factory
    factory = read_factory()

    # use the factory to create the media exporter
    media_exporter = factory()

    # perform the exporting job
    do_export(media_exporter)


if __name__ == '__main__':
    main()
