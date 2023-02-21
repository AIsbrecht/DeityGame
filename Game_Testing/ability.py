from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from base_component import BaseComponent

from entity import Actor
import ai
import color
import actions

class Ability(BaseComponent):
    parent: Actor

    def __init__(self, ability: Ability):
        self.ability = ability

class Rooted(Ability):
    def activate(self, action: actions.BumpAction, number_of_turns) -> None:
        target = action.target_actor

        self.engine.message_log.add_message(
                f"The {target.name} becomes rooted in place!",
                color.status_effect_applied,
            )
        target.ai = ai.RootedEnemy(
                entity=target, previous_ai=target.ai, turns_remaining=self.number_of_turns,
            )
class Default(Ability):   
    def activate():
        pass

class Shocking(Ability):
    def activate(self, action: actions.BumpAction, number_of_turns) -> None:
        target = action.target_actor

        self.engine.message_log.add_message(
                f"The {target.name} gets shocked!",
                color.status_effect_applied,
            )
        target.ai = ai.ShockedEnemy(
                entity=target, previous_ai=target.ai, turns_remaining=self.number_of_turns,
            )

class Defender(Ability):
    def activate(self, action: actions.BumpAction, cooldown) -> None:
        target = action.target_actor
        self.engine.message_log.add_message(
                    f"The {target.name} gets shocked!",
                    color.status_effect_applied,
                )

class Healer(Ability):
    def activate(self, action: actions.PickupAction) -> None:
        self.engine.message_log.add_message(
                    f"You get a second {actions.item.name}",
                    color.status_effect_applied,
                )

class Bloodlust(Ability):
    def activate(self, action: actions.BumpAction) -> None:
        target = action.target_actor
        #use a custom actions to attack multiple enemies

class Lust(Ability):
    def activate(self, action: actions.BumpAction, cooldown) -> None:
        target = action.target_actor
        self.engine.message_log.add_message(
                    f"The {target.name} gets shocked!",
                    color.status_effect_applied,
                )