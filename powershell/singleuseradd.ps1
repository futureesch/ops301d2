# Author - Tom Esch
# Date Last Revised - 3/10/2021
# Purpose - Automate adding useres to ADAC

New-ADUser -Name "FranzFerdinand" -OtherAttributes @{'title'="TPS Reporting Lead":"ferdi@GlobeXpower.com"}

