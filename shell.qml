import QtQuick
import Quickshell
import Quickshell.Io

Item {
    Process{
        command: ["python",Qt.resolvedUrl("python/main.py")]
        running: true
    }

}