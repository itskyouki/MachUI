import Quickshell
import QtQuick
import Quickshell.Io
import Quickshell.Wayland

PanelWindow {
    id: home
    visible: false
    WlrLayershell.layer: WlrLayer.Overlay

    anchors {
        top: true
        left: true
        right: true
    }

    margins {
        top: -3
        left: 350
        right: 350
    }

    implicitHeight: 500
    color: "transparent"

    Rectangle {
        anchors.fill: parent

        color: "#080808"
        topLeftRadius: 0
        topRightRadius: 0
        bottomLeftRadius: 10
        bottomRightRadius: 10
        border.width: 1
        border.color: "white"

        Rectangle {
            anchors {
                top: parent.top
                left: parent.left
                right: parent.right
            }

            height: 2
            color: "black"
        }
    }

    IpcHandler {
        target: "home"

        function toggle(): void {
            home.visible = !home.visible
        }
    }
}