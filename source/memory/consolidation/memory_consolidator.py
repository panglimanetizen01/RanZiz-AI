"""
RanZiz AI Memory Consolidator
Version 1.0
"""

from datetime import UTC, datetime


class MemoryConsolidator:


    def consolidate(

        self,

        memories

    ):

        result = {}


        for key, item in memories.items():


            if isinstance(item, dict):

                item["frequency"] = item.get(

                    "frequency",

                    0

                ) + 1


                item["last_seen"] = datetime.now(UTC).isoformat()


                result[key] = item


            else:

                result[key] = {

                    "value": item,

                    "frequency": 1,

                    "last_seen": datetime.now(UTC).isoformat()

                }


        return result



    def strengthen(

        self,

        memory

    ):

        if "priority" in memory:

            memory["priority"] += 1


        return memory



    def __repr__(self):

        return "MemoryConsolidator()"