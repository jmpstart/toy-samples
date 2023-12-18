![Vamos](./.vamos/toy-samples.jpg)

# Toy Samples

Let us experience a rapid setup process for play ground `toy-samples` with minimal user
interaction using `vamos` (a `playground manager`).

-----------------------------------------------------------------------------------------------

## Step 1: Install Vamos

This step is only required if `vamos` is not yet installed and can otherwise be omitted.
In a `BASH` shell with `git` and `python3` installed run the following `curl` formula:

```
  curl https://raw.githubusercontent.com/jmpstart/vamos/main/install >~vamos; source ~vamos -s
```
-----------------------------------------------------------------------------------------------


## Step 2: Clone and Setup Playground

With `vamos` installed, choose a convenient working directory for creation of a
git repository folder `toy-samples` by invoking:

```
    vamos @jmpstart/toy-samples
```

This causes `vamos` to clone repository https://github.com/jmpstart/toy-samples
and setup a playground (toy-samples) managed by a virtual Python environment
`@toy`. In case of a success message you also get a hint
that command `?` has been provided for quick help regarding the playground.

```
    ...
    playground @toy setup complete!
    type ? for quick help
    (@toy) $
```

Also note the character sequence `(@toy)` as part of the command line prompt, which indicates
that the virtual environment of the playground is activated.
If for any reason (e.g., open a new console/terminal window) `cd` to the playground's home
folder (`toy-samples`) and invoke `$ . vamos` to re-activate the playground.

--------------------------------------------------------------------------------

# Exploring the Playground

Get quick help by hitting the `?` command:

```
    (@toy) $ ?
    Utilities, coming with playground @toy (toy-samples)
      ecco          # echo colored text
      gil           # log git commit history
      wd            # change working directory
      casino        # print random roulette numbers
      prompt        # change prompt to recommended one
    try these commands with -? or --help option to get additional help
    (@toy) $
```

## Ecco - Echo Colored text

```
    (@toy) $ ecco -?
    usage: ecco ...     # (uncolored) echo ...
           ecco -r ...  # (red)
           ecco -g ...  # (green)
           ecco -y ...  # (yellow)
           ecco -b ...  # (blue)
           ecco -m ...  # (magenta)
           ecco -c ...  # (cyan)
           ecco -n ...  # (no color)    
    (@toy) $ ecco -g 'the opperation was successful!'
    the opperation was successful!
```


## Gil - Git Log in Tree Form

```
    (@toy) $ gil
    * c074d89 (HEAD -> main, origin/main, origin/HEAD) ...
    ...
```


## Wd - Change Working Directory

```
    (@toy) $ wd -?
    usage: wd ...       # change working directory / virtual environment
           wd <path>    # change current dir, occasionally switch venv
           wd .         # store working directory in WORKDIR
           wd           # change to $WORKDIR
           wd -?        # help
           wd --help    # help

           activate new virtual environment if such is found in current
           directory or in parent directory hierarchy.```
```

## Casino - Generate Random Numbers

```
    (@toy) $ casino -?
    usage: casino         # get random number (0 <= n <= 36)
           casino <n>     # n times get random number
           casino -?      # show help
           casino --help  # show help
```

## Prompt - Set Standard Prompt

```
(@toy) ... $ prompt
(@toy) toy-samples $
```

--------------------------------------------------------------------------------

# Appendix: Vamos Installation Process

Invoking command

```
    $ vamos @jpmstart/toy-samples
```

runs a two-phase `vamos` installation process. In phase 1 the following three steps are performed:

* clone repository ´https://github.com/jmpstart/toy-samples.git into a new created folder `./toy-samples`
* subsequently the working directory is changed to this folder
* and startup script ./.vamos/bin/startup is `sourced` (executed in current BASH environment)

In phase 2 the specific startup script of
playground `toy-samples` (located in `.vamos/bin/startup`) is executed:

* create a `venv` folder representing a virtual Python environment
* activate the vitual Python environment
* upgrade Python `pip` package
* install another Python package
* copy of some BASH scripts (our `toy samples`) from .vamos/bin into venv/bin
* provide a quick help command to be invoked by `$ ?`
