import Quickshell
import QtQuick

PanelWindow {
    anchors {
        top: true
        left: true
        right: true
    }
    margins{
        top: 10
        left: 18
        right: 18
    }

    implicitHeight: 40
    color: "transparent"

    Rectangle {
        anchors.fill: parent

        color: "#080808"
        border.width: 1
        border.color: "#FFFFFF"
        radius: 10

        Text {
            anchors.centerIn: parent

            text: "text box, put the dumped clock.json from the clock.py module"

            color: "#ffffff"
            font.family: "monospace"
            font.pixelSize: 10
            font.bold: false
        }
    }
}