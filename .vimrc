colo elflord
set nocompatible              " be iMproved, required
filetype off                  " required
filetype plugin on " for vimwiki
syntax on
"
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
	call vundle#begin()
	"" alternatively, pass a path where Vundle should install plugins
	""call vundle#begin('~/some/path/here')
"
"" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
"Plugin 'vim-scripts/Conque-GDB' " For shell in vim
"" The following are examples of different formats supported.
"" Keep Plugin commands between vundle#begin/end.
"" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
Plugin 'itchyny/lightline.vim'
Plugin 'suoto/vim-hdl'
Plugin 'vim-syntastic/syntastic'
Plugin 'ervandew/supertab'
""Plugin 'vim-scripts/TagHighlight'
Plugin 'octol/vim-cpp-enhanced-highlight'
Plugin 'dpelle/vim-LanguageTool'
Plugin 'vimwiki/vimwiki'
""plugin from http://vim-scripts.org/vim/scripts.html
"" Plugin 'L9'
"" Git plugin not hosted on GitHub
""Plugin 'git://git.wincent.com/command-t.git'
"" git repos on your local machine (i.e. when working on your own plugin)
""Plugin 'file:///home/gmarik/path/to/plugin'
"" The sparkup vim script is in a subdirectory of this repo called vim.
"" Pass the path to set the runtimepath properly.
"":Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
"" Install L9 and avoid a Naming conflict if you've already installed a
"" different version somewhere else.
"" Plugin 'ascenator/L9', {'name': 'newL9'}
"
"" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
""filetype plugin on
""
"" Brief help
"" :PluginList       - lists configured plugins
"" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
"" :PluginSearch foo - searches for foo; append `!` to refresh local cache
"" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
""
"" see :h vundle for more details or wiki for FAQ
"" Put your non-Plugin stuff aft"
set number

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
" [buffer number] followed by filename:
set statusline=[%n]\ %t
" show line#:column# on the right hand side
set statusline+=%=%l:%c
autocmd CursorMoved * exe printf('match IncSearch /\V\<%s\>/', escape(expand('<cword>'), '/\'))
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['pylint','python']
"let g:syntastic_vhdl_checkers = ['vimhdl']

" Configure the project file
let g:vimhdl_conf_file = '<config/file>'
" " Tell Syntastic to use vim-hdl
let g:syntastic_vhdl_checkers = ['ghdl']


" netrw for tree

let g:netrw_banner = 0
let g:netrw_liststyle = 3
"let g:netrw_browse_split = 2
"" let g:netrw_altv = 1
let g:netrw_winsize = 25
""augroup ProjectDrawer
	 " autocmd!
	  "  autocmd VimEnter * :Vexplore
  "  augroup END
" for lightline plugin
set laststatus=2 
" For showing the 256 color scheme, in bashrc include:
" export TERM=xterm-256color
if !has('gui_running')
  set t_Co=256
endif
set noshowmode
" Language tool 
let g:languagetool_jar='/home/sal/LanguageTool_4_4/languagetool-commandline.jar'
"" WIKI HANDLER


function! VimwikiLinkHandler(link)
  " Use Vim to open external files with the 'vfile:' scheme.  E.g.:
  "   1) [[vfile:~/Code/PythonProject/abc123.py]]
  "   2) [[vfile:./|Wiki Home]]
  let link = a:link
  if link =~# '^vfile:'
    let link = link[1:]
  else
    return 0
  endif
  let link_infos = vimwiki#base#resolve_link(link)
  if link_infos.filename == ''
    echomsg 'Vimwiki Error: Unable to resolve link!'
    return 0
  else
    exe 'tabnew ' . fnameescape(link_infos.filename)
    return 1
  endif
endfunction

" From https://blog.mague.com/?p=602 
let g:vimwiki_list = [
                       \{'path': '~/vimwiki/work/'},
                       \{'path': '~/vimwiki/personal/'},
                       \{'path': '~/vimwiki/lmtpedia/'}
		\]
au BufRead,BufNewFile *.wiki set filetype=vimwiki
:autocmd FileType vimwiki map d :VimwikiMakeDiaryNote


