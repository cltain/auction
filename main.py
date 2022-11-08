from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program")
def highest(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in (bidding_record):
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
choice = True
auction = {}
while choice:
  name = input("What is your name?: \n")
  bid = input("What is your bid?: \n")
  auction[name] = bid 
  more = input("Are there any other bidders?: Type 'yes' or 'no'.\n")
  if more == "yes":
    clear()
  else:
    choice = False
    highest(auction)
