from pathlib import Path

from processing.core.ProcessingConfig import ProcessingConfig

from ..text_constants import TextConstants
from ..utils import log


class QMapshaperPaths:

    @staticmethod
    def full_path_command(command: str) -> str:

        mapshaper_bin_folder = QMapshaperPaths.mapshaper_bin_folder()

        if mapshaper_bin_folder:

            path = Path(mapshaper_bin_folder) / command

            return path.absolute().as_posix()

        else:
            return command

    @staticmethod
    def mapshaper_bin_folder() -> str:

        mapshaper_folder = QMapshaperPaths.mapshaper_folder()

        if mapshaper_folder:
            folder = Path(mapshaper_folder) / "bin"

            return folder.absolute().as_posix()

        return ""

    @staticmethod
    def mapshaper_folder() -> str:

        folder = ProcessingConfig.getSetting(TextConstants.MAPSHAPER_FOLDER)

        if not folder:
            folder = QMapshaperPaths.guess_mapshaper_folder()

        return folder if folder else ''

    @staticmethod
    def guess_mapshaper_folder() -> str:

        from .class_qmapshaper_runner import MapshaperProcessChecker, NpmPackageLocationCheckerProcess

        # globally available
        mp = MapshaperProcessChecker("")
        if mp.found:
            return ""

        npm_checker = NpmPackageLocationCheckerProcess()

        folder = npm_checker.mapshaper_path()

        mp = MapshaperProcessChecker(folder)
        if mp.found:
            return mp.path

        return ""

    @staticmethod
    def mapshaper_command_name():
        return "mapshaper-xl"

    @staticmethod
    def mapshaper_command_call() -> str:

        mapshaper_bin_folder = QMapshaperPaths.mapshaper_bin_folder()

        if mapshaper_bin_folder:

            bin_path = Path(mapshaper_bin_folder)

            bin_path = bin_path / QMapshaperPaths.mapshaper_command_name()

            return bin_path.absolute().as_posix()

        else:

            return QMapshaperPaths.mapshaper_command_name()
