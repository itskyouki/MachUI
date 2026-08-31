import Quickshell
import QtQuick
import Quickshell.Io

FloatingWindow{
    id: launcher
    visible: true
    width: 200
    height: 100
    Text{
        anchors.centerIn: parent
        text: "Hello Quickshell"
        font.pixelSize: 18
    }
    IpcHandler {
        target: "launcher"

        function toggle(): void {
            launcher.visible = !launcher.visible
        }
    }
}