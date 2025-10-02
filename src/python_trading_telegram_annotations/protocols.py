"""Protocoles et interfaces pour le typage."""

from typing import Any, Dict, List, Optional, Protocol, Union

from python_trading_telegram_annotations.classes.command import Command
from python_trading_telegram_annotations.classes.enums import DynamicEnumMember


class HandlerProtocol(Protocol):
    """Protocole définissant l'interface d'un handler."""

    def process_command(
            self,
            cmd: Union[Command, DynamicEnumMember],
            arguments: List[Any]
    ) -> Optional[Dict[str, Any]]:
        """Traite une commande avec ses arguments.
        
        Args:
            cmd: La commande à exécuter
            arguments: Les arguments de la commande
            
        Returns:
            Dict avec la réponse ou None
        """
        ...
