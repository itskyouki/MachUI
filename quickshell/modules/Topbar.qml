import Quickshell
import QtQuick

PanelWindow {
  anchors {
    top: true
    left: false
    right: false
  }

  implicitHeight: 30
  implicitWidth: 1270

  Text {
    // center the bar in its parent component (the window)
    anchors.centerIn: parent

    text: "text box, put the dumped clock.json from the clock.py module"
  }
}