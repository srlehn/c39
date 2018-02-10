#!/usr/bin/env python3


################################################################################
class barcode:
  def __init__(self, str="", barcode_type="", image_type=""):
    self.str = str
    self.barcode_type = barcode_type
    self.image_type = image_type

    self.barcode_linear = ''
    self.sixel = ''

    self.barcode_linear_width = 50

    self.barcode_thick_line_width = 6
    self.barcode_thin_line_width  = 2


    self.convert_string()
    self.enlarge_barcode()
    self.convert_barcode()

    #print(self.barcode_linear)
    print("\n  " + self.sixel)


  ##############################################################################
  def convert_string(self):
    if self.barcode_type == "code39":
      self.convert_string_to_code39()
      return


  ##############################################################################
  def convert_string_to_code39(self):
    map = {
      '1' : '110100101011',
      '2' : '101100101011',
      '3' : '110110010101',
      '4' : '101001101011',
      '5' : '110100110101',
      '6' : '101100110101',
      '7' : '101001011011',
      '8' : '110100101101',
      '9' : '101100101101',
      '0' : '101001101101',
      'A' : '110101001011',
      'B' : '101101001011',
      'C' : '110110100101',
      'D' : '101011001011',
      'E' : '110101100101',
      'F' : '101101100101',
      'G' : '101010011011',
      'H' : '110101001101',
      'I' : '101101001101',
      'J' : '101011001101',
      'K' : '110101010011',
      'L' : '101101010011',
      'M' : '110110101001',
      'N' : '101011010011',
      'O' : '110101101001',
      'P' : '101101101001',
      'Q' : '101010110011',
      'R' : '110101011001',
      'S' : '101101011001',
      'T' : '101011011001',
      'U' : '110010101011',
      'V' : '100110101011',
      'W' : '110011010101',
      'X' : '100101101011',
      'Y' : '110010110101',
      'Z' : '100110110101',
      '-' : '100101011011',
      '.' : '110010101101',
      ' ' : '100110101101',
      '*' : '100101101101',
    }

    str = '*' + self.str.upper().replace('*', '_') + '*'

    barcode_temp = [map[char] + '0' if char in map else map['-'] + '0' for char in str]
    self.barcode_linear = ''.join(barcode_temp)[:-1]


  ##############################################################################
  def convert_barcode(self):
    if self.image_type == "sixel":
      self.convert_barcode_to_sixel()
      return


  ##############################################################################
  def enlarge_barcode(self):
    self.barcode_linear = self.barcode_linear\
    .replace('00', '2')\
    .replace('11', '3')\
    .replace('0', '0' * self.barcode_thin_line_width)\
    .replace('1', '1' * self.barcode_thin_line_width)\
    .replace('2', '0' * self.barcode_thick_line_width)\
    .replace('3', '1' * self.barcode_thick_line_width)  


  ##############################################################################
  def convert_barcode_to_sixel(self):
    if self.barcode_linear:
      self.convert_barcode_to_sixel_linear()
      return
      

  ##############################################################################
  def convert_barcode_to_sixel_linear(self):
    self.sixel = "\033Pq"

    filler = 6 - len(self.barcode_linear) % 6
    if filler == 6:
      filler = 0

    self.barcode_linear += '0' * filler

    bc = self.barcode_linear

    while len(bc) != 0:
      sixel_char = chr(63 + int(bc[:6][::-1], 2))
      bc = bc[6:]

      self.sixel += '!' + str(self.barcode_linear_width) + sixel_char + '-'

    self.sixel = self.sixel[:-1] + "\033\\"


################################################################################
def main():
  barcode(str="tes((t", barcode_type="code39", image_type="sixel")


################################################################################
if __name__ == "__main__":
  main()
