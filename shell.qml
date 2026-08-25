import Quickshell
import Quickshell.Io
import "quickshell"

ShellRoot {
    Process {
        command: ["/usr/bin/python", Quickshell.shellPath("python/main.py")]
        running: true
    }

    Main {}
}