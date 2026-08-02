from source.core.brain import Brain
from source.plugins.plugin_manager import PluginManager


def main():

    plugin_manager = PluginManager()

    brain = Brain()


    print("=" * 40)
    print(brain.startup())
    print("=" * 40)


    plugins = plugin_manager.list_plugins()


    if plugins:

        print("\nPlugin berhasil dimuat:")

        for name in plugins:
            print(f"- {name}")


        print(
            f"\nPlugin aktif : {plugin_manager.active_name()}"
        )


    else:

        print(
            "\nTidak ada plugin yang dimuat."
        )



    while True:

        user = input("\nKamu : ")


        if user.lower() in [
            "exit",
            "quit",
            "keluar"
        ]:

            print(
                "RanZiz AI : Sampai jumpa."
            )

            break



        reply = brain.process(
            user
        )


        print(
            "RanZiz AI :",
            reply
        )



if __name__ == "__main__":

    main()
