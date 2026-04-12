from Plugins.Plugin import PluginDescriptor
from . import wol
import enigma
from . import _


def configure(session, iface=None, **kwargs):
    try:
        from . import ui
        session.openWithCallback(doneConfiguring, ui.WakeOnLanConfig)
    except Exception as ex:
        print("[WOL] Sorry, UI failed to start:", ex)


def sendnow(session=None, iface=None, **kwargs):
    try:
        wol.sendAllWOL()
    except Exception as ex:
        print("[WOL] failed to send out WOL packets:", ex)


def doneConfiguring(session, retval):
    pass


def gotRecordEvent(service, event):
    if event == enigma.iRecordableService.evStart:
        sendnow()


def autostart(reason, session=None, **kwargs):
    "called with reason=1 to during shutdown, with reason=0 at startup"
    if session and not reason:
        session.nav.record_event.append(gotRecordEvent)


DESCRIPTION = _("Send WOL packet on PVR and recording start")


def Plugins(**kwargs):
    return [
        PluginDescriptor(
            name="Wake-On-LAN",
            description=DESCRIPTION,
            where=[PluginDescriptor.WHERE_SESSIONSTART],
            fnc=autostart,
        ),
        PluginDescriptor(
            name=_("Configure Wake-On-LAN"),
            description=DESCRIPTION,
            where=PluginDescriptor.WHERE_NETWORKSETUP,
            fnc={
                "ifaceSupported": lambda x: configure,
                "menuEntryName": lambda x: _("Configure Wake-on-LAN"),
                "menuEntryDescription": lambda x: DESCRIPTION,
            },
        ),
        PluginDescriptor(
            name=_("Send Wake-On-LAN"),
            description=DESCRIPTION,
            where=PluginDescriptor.WHERE_NETWORKSETUP,
            fnc={
                "ifaceSupported": lambda x: sendnow,
                "menuEntryName": lambda x: _("Send Wake-on-LAN"),
                "menuEntryDescription": lambda x: DESCRIPTION,
            },
        ),
    ]
