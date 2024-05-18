"""
This script will change an ASG's minimum value from '0' to '1'
"""
import boto3
from termcolor import colored
import sys

CLIENT = boto3.client("autoscaling")

ASGS = [
    "asg-frontend",
    "asg-workers",
]


def change_minimum_to_one(asgname):
    """
    This script will change an ASG's minimum value from '0' to '1'
    """
    
    response = CLIENT.update_auto_scaling_group(
        AutoScalingGroupName=asgname,
        MinSize=1,
    )
    if response["ResponseMetadata"]["HTTPStatusCode"] is 200:
        print(
            "\n- %s" % colored("SUCCESS:", "green"),
            "The minimum of ASG Group:",
            asgname,
            "is now set to 1.",
        )
    else:
        print(
            "%s" % colored("FAILED:", "red"),
            "Minimum of ASG group could not be changed.\n",
        )


if __name__ == "__main__":

    def confirm():
        print("Here are the ASG's that will be switched on: \n")
        for asg in ASGS:
            print("- %s" % asg)
        USER_INPUT = input("\nProceed? (y/n): ")
        return USER_INPUT

    USER_INPUT = confirm()

    if USER_INPUT is "y" or USER_INPUT is "Y":
        for asg in ASGS:
            change_minimum_to_one(asg)
        print("\n")

    elif USER_INPUT is not "y":  # If someone types something that's not 'y' or 'n'
        if USER_INPUT is not "n":
            print(colored("\nInvalid entry. Let's try again.\n", "red"))
            main()

    if USER_INPUT is "n": or USER_INPUT is "N":
        print("\nGood bye!\n")
        sys.exit(1)
