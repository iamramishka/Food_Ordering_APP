{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "649cf730",
   "metadata": {},
   "source": [
    "# Food Delivery Agent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "067dd6ed-ee54-438b-8f02-f39979485623",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Food Delivery! Here are the items we have:\n",
      "Pizza - $8\n",
      "Burger - $5\n",
      "Pasta - $7\n",
      "Salad - $4\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Please type the item(s) you want to order (separate with commas if more than one):  Pizza,Pasta\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "You have chosen Pizza, Pasta. The total is $15.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Please provide your delivery address:  Matara\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Order confirmed! Your order will be delivered to Matara.\n"
     ]
    }
   ],
   "source": [
    "# Food Delivery Agent\n",
    "\n",
    "menu = {\n",
    "    \"Pizza\": 8,\n",
    "    \"Burger\": 5,\n",
    "    \"Pasta\": 7,\n",
    "    \"Salad\": 4\n",
    "}\n",
    "\n",
    "def display_menu():\n",
    "    print(\"Welcome to Food Delivery! Here are the items we have:\")\n",
    "    for item, price in menu.items():\n",
    "        print(f\"{item} - ${price}\")\n",
    "\n",
    "        \n",
    "#Calculate Total Items\n",
    "def calculate_total(selected_items):\n",
    "    total = sum(menu[item] for item in selected_items)\n",
    "    return total\n",
    "\n",
    "def main():\n",
    "    display_menu()\n",
    "    \n",
    "    user_input = input(\"\\nPlease type the item(s) you want to order (separate with commas if more than one): \").strip()\n",
    "    selected_items = [item.strip() for item in user_input.split(\",\") if item.strip() in menu]\n",
    "    \n",
    "    if not selected_items:\n",
    "        print(\"You didn't select any valid items. Please try again.\")\n",
    "        return\n",
    "    \n",
    "    total_cost = calculate_total(selected_items)\n",
    "    print(f\"\\nYou have chosen {', '.join(selected_items)}. The total is ${total_cost}.\")\n",
    "    \n",
    "    delivery_address = input(\"\\nPlease provide your delivery address: \").strip()\n",
    "    if delivery_address:\n",
    "        print(f\"\\nOrder confirmed! Your order will be delivered to {delivery_address}.\")\n",
    "    else:\n",
    "        print(\"\\nYou didn't provide an address. Please try again.\")\n",
    "\n",
    "# Call to the Main Function\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4e5ce71-6536-4ad7-af0f-34fe3d378508",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
