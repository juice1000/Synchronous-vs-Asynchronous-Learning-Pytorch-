import matplotlib.pyplot as plt
from numpy import loadtxt
import argparse
import numpy as np

def handleArguments():
    """Handles CLI arguments and saves them globally"""
    parser = argparse.ArgumentParser(
        description="Switch between modes in A2C or loading models from previous games")
    parser.add_argument("--a2c", "-2", help="Takes data from A2C agents", action="store_true")
    parser.add_argument("--a3c", "-3", help="Takes data from A3C agents", action="store_true")
    parser.add_argument("--a2csync", "-S", help="Takes data from A2C-Sync agents", action="store_true")
    parser.add_argument("--separatedNN", "-se", help="Takes data from separated NN agents", action="store_true")
    parser.add_argument("--sharedNN", "-sh", help="Takes data from shared NN agents", action="store_true")
    parser.add_argument("--all", "-a", help="Takes data from all agents", action="store_true")
    parser.add_argument("--test", "-t", help="Takes data from all agents", action="store_true")
    global args
    args = parser.parse_args()
    return args

def plotter_ep_rew_all(scores, label):
    plt.plot(scores, label=label)
    plt.axhline(y=0, color='r')
    plt.ylim(-120,450)
    plt.ylabel('Reward per Episode')
    plt.xlabel('Episode')


if __name__ == "__main__":

    args = handleArguments()

    if args.test:
        if args.a2c:
            # load array
            a2c_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_test.csv', delimiter=',')
            a2c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_comb_test.csv', delimiter=',')

            plotter_ep_rew_all(a2c_data, "A2C")
            plotter_ep_rew_all(a2c_comb_data, "A2C (shared NN)")

        if args.a3c:
            # load array
            a3c_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_test.csv', delimiter=',')
            a3c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_comb_test.csv', delimiter=',')

            plotter_ep_rew_all(a3c_data, "A3C")
            plotter_ep_rew_all(a3c_comb_data, "A3C (shared NN)")

        if args.a2csync:
            # load array
            a2c_sync_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_test.csv', delimiter=',')
            a2c_sync_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_comb_test.csv', delimiter=',')

            plotter_ep_rew_all(a2c_sync_data, "A2C-Sync")
            plotter_ep_rew_all(a2c_sync_comb_data, "A2C-Sync (shared NN)")

        if args.separatedNN:
            # load array
            a2c_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_test.csv', delimiter=',')
            a3c_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_test.csv', delimiter=',')
            a2c_sync_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_test.csv', delimiter=',')

            plotter_ep_rew_all(a2c_data, "A2C")
            plotter_ep_rew_all(a3c_data, "A3C")
            plotter_ep_rew_all(a2c_sync_data, "A2C-Sync")

        if args.sharedNN:
            # load array
            a2c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_comb_test.csv', delimiter=',')
            a3c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_comb_test.csv', delimiter=',')
            a2c_sync_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_comb_test.csv', delimiter=',')

            plotter_ep_rew_all(a2c_comb_data, "A2C (shared NN)")
            plotter_ep_rew_all(a3c_comb_data, "A3C (shared NN)")
            plotter_ep_rew_all(a2c_sync_comb_data, "A2C-Sync (shared NN)")

        if args.all:
            # load array
            # load array
            a2c_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_test.csv', delimiter=',')
            a3c_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_test.csv', delimiter=',')
            a2c_sync_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_test.csv', delimiter=',')

            plotter_ep_rew_all(a2c_data, "A2C")
            plotter_ep_rew_all(a3c_data, "A3C")
            plotter_ep_rew_all(a2c_sync_data, "A2C-Sync")

            # load array
            a2c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_comb_test.csv', delimiter=',')
            a3c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_comb_test.csv', delimiter=',')
            a2c_sync_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_comb_test.csv', delimiter=',')

            plotter_ep_rew_all(a2c_comb_data, "A2C (shared NN)")
            plotter_ep_rew_all(a3c_comb_data, "A3C (shared NN)")
            plotter_ep_rew_all(a2c_sync_comb_data, "A2C-Sync (shared NN)")

    else:
        if args.a2c:
            # load array
            a2c_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom.csv', delimiter=',')
            a2c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_comb.csv', delimiter=',')

            plotter_ep_rew_all(a2c_data, "A2C")
            plotter_ep_rew_all(a2c_comb_data, "A2C (shared NN)")

        if args.a3c:
            # load array
            a3c_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom.csv', delimiter=',')
            a3c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_comb.csv', delimiter=',')

            plotter_ep_rew_all(a3c_data, "A3C")
            plotter_ep_rew_all(a3c_comb_data, "A3C (shared NN)")

        if args.a2csync:
            # load array
            a2c_sync_arr = []
            for i in range(1, 44):
                a2c_sync_data = loadtxt(f'VIZDOOM/doom_save_plot_data/A2C/a2c_sync_doom{i}.csv', delimiter=',')
                if a2c_sync_data != []:
                    for j in a2c_sync_data:
                       a2c_sync_arr.append(j)

            plotter_ep_rew_all(a2c_sync_arr, "A2C-Sync")

            a2c_sync_comb_arr = []
            for j in range(1,43):
                a2c_sync_comb_data = loadtxt(f'VIZDOOM/doom_save_plot_data/A2C_Comb/a2c_sync_doom_comb{j}.csv', delimiter=',')
                if a2c_sync_comb_data != []:
                    for j in a2c_sync_comb_data:
                        a2c_sync_comb_arr.append(j)

            plotter_ep_rew_all(a2c_sync_comb_arr, "A2C-Sync (shared NN)")


        if args.separatedNN:
            # load array
            a2c_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom.csv', delimiter=',')
            a3c_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom.csv', delimiter=',')
            a2c_sync_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom.csv', delimiter=',')

            plotter_ep_rew_all(a2c_data, "A2C")
            plotter_ep_rew_all(a3c_data, "A3C")
            plotter_ep_rew_all(a2c_sync_data, "A2C-Sync")

        if args.sharedNN:
            # load array
            a2c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_comb.csv', delimiter=',')
            a3c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_comb.csv', delimiter=',')
            a2c_sync_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_comb.csv', delimiter=',')

            plotter_ep_rew_all(a2c_comb_data, "A2C (shared NN)")
            plotter_ep_rew_all(a3c_comb_data, "A3C (shared NN)")
            plotter_ep_rew_all(a2c_sync_comb_data, "A2C-Sync (shared NN)")

        if args.all:
            # load array
            # load array
            a2c_data = loadtxt('VIZDOOM/cart_save_plot_data/a2c_doom.csv', delimiter=',')
            a3c_data = loadtxt('VIZDOOM/cart_save_plot_data/a3c_doom.csv', delimiter=',')
            a2c_sync_data = loadtxt('VIZDOOM/cart_save_plot_data/a2c_sync_doom.csv', delimiter=',')

            plotter_ep_rew_all(a2c_data, "A2C")
            plotter_ep_rew_all(a3c_data, "A3C")
            plotter_ep_rew_all(a2c_sync_data, "A2C-Sync")

            # load array
            a2c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_doom_comb.csv', delimiter=',')
            a3c_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a3c_doom_comb.csv', delimiter=',')
            a2c_sync_comb_data = loadtxt('VIZDOOM/doom_save_plot_data/a2c_sync_doom_comb.csv', delimiter=',')

            plotter_ep_rew_all(a2c_comb_data, "A2C (shared NN)")
            plotter_ep_rew_all(a3c_comb_data, "A3C (shared NN)")
            plotter_ep_rew_all(a2c_sync_comb_data, "A2C-Sync (shared NN)")



    plt.legend()
    plt.show()