---
Category: note
Date: '2022-05-20'
Modified: '2023-07-12'
Slug: bash-encode-decode-base64-and-hex
Status: published
Tags: base64, bash, decode, encode, hex
Title: Bash - Encode, Decode Base64 and Hex
---

## Tools

`xxd` - make a hexdump or do the reverse.
`base64` - base64 encode/decode data and print to standard output

## Encode hex

```sh
echo "hello" | xxd -p
68656c6c6f0a
```

## Decode hex

```sh
echo "68656c6c6f0a" | xxd -r -p
```

## Encode base64

```sh
echo "hello" | base64
aGVsbG8K
```

## Decode base64

```sh
echo "aGVsbG8K" | base64 --decode
```

## Encode/decode ROT13

```sh
echo "Hello" | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
```

## Caesar cipher encoding

(from: <https://gist.github.com/IQAndreas/030b8e91a8d9a407caa6>)
The Caesar Cipher shifts plaintext three letters to the left to create ciphertext.

In this case, `tr '[A-Z]' '[X-ZA-W]'`, tr translates all occurrences of 'A' to 'X', 'B' to 'Y', 'C' to 'Z', 'D' to 'A', etc.

`[X-ZA-W]` just means that your output starts with the letter X and continues through the letter Z, then continues with the letter A through the letter W. You could also use `[XYZABCDEFGHIJKLMNOPQRSTUVW]` instead but tr understands the hyphen '-' to mean 'through'.

```sh
echo "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG" | tr '[A-Z]' '[X-ZA-W]'
QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
```

## Caesar cipher decoding

```sh
echo "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD" | tr '[X-ZA-W]' '[A-Z]'
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
```
