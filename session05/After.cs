using System;
using System.Collections.Generic;
using System.Linq;

namespace Exercise {

    public class ArticleStatus {
        public int Id { get; set; }
        public string Name { get; set; }
    }

    public class Article {
        public bool? HiddenByReviewer { get; set; }
        public ArticleStatus Status { get; set; }
        public long ReviewCode { get; set; }
        public string Name { get; set; }
    }

    public class UserFilter {
        public string Value { get; set; }
        public string Logic { get; set; }
        public string Operator { get; set; }

        public bool IsBasicFilter() {
            return Logic.Equals("or") && Operator.Equals("contains");
        }

        public IEnumerable<Article> RunFilter(IEnumerable<Article> data) {
            if (IsBasicFilter()) {
                return(
                    data.Where(
                        t => ( 
                            t.Name.Contains(this.Value, StringComparison.OrdinalIgnoreCase) ||
                            string.Format("THING#{0}", t.ReviewCode.ToString().PadLeft(10, '0')).Contains(this.Value, StringComparison.OrdinalIgnoreCase)
                        )
                    )
                );
            } else {
                return data;
            }
        }
    }
    
    public enum Tab {
        WorkInProgress,
        SubmittedForReview,
        Accepted,
        Completed
    }

    public class Column {
        public static Column Make(Tab col) {
            switch (col) {
                case Tab.Accepted: return new AcceptedColumn();
                case Tab.Completed: return new CompletedColumn();
                default: return new Column();
            }
        }
        public virtual IEnumerable<Article> RunColumnFilter(IEnumerable<Article> data) {
            return data;
        }
        public virtual IEnumerable<Article> RunUserFilter(IEnumerable<Article> data, UserFilter user_filter) {
            return data;
        }
        public IEnumerable<Article> RunBothFilters(IEnumerable<Article> data, UserFilter user_filter ) {
            return RunUserFilter(RunColumnFilter(data), user_filter);
        }
    }

    public abstract class FilteringColumn : Column {
        public override IEnumerable<Article> RunUserFilter(IEnumerable<Article> data, UserFilter user_filter) {
            return user_filter.RunFilter(data);
        }
    }

    public class AcceptedColumn : FilteringColumn {
        public override IEnumerable<Article> RunColumnFilter(IEnumerable<Article> data) {
            return data.Where(p => !p.HiddenByReviewer.HasValue || !p.HiddenByReviewer.Value);
        }
    }

    public class CompletedColumn : FilteringColumn {
        public override IEnumerable<Article> RunColumnFilter(IEnumerable<Article> data) {
            return(
                data.Where(
                    p => (
                        (p.HiddenByReviewer.HasValue == true && p.HiddenByReviewer.Value == true) ||
                        (p.Status != null && p.Status.Id == 9)
                    )
                )
            );
        }
    }

    public class Exercise {
        private static IEnumerable<Article> FilterProposals(IEnumerable<Article> dataToFilter, UserFilter user_filter, Column column) {
            if (user_filter == null || column == null) throw new ArgumentNullException();
            return column.RunBothFilters(dataToFilter, user_filter);
        }       
        public static IEnumerable<Article> FilterProposals(IEnumerable<Article> dataToFilter, UserFilter user_filter, Tab col) {
            return FilterProposals(dataToFilter, user_filter ?? new UserFilter(), Column.Make(col));
        }
    }
}