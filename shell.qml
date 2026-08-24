import Quickshell
import Quickshell.Io
import "quickshell"


ShellRoot {
    Process {
        command: ["python", Quickshell.shellPath("python/main.py")]
        running: true
    }

    Main {}
}